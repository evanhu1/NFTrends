import React, { Component, useEffect } from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import { tableCellClasses } from "@mui/material/TableCell";
import { Container } from '@mui/material';
import Typography from '@mui/material/Typography';
import './Rankings.css';

const columns = [
    { id: 'rank', label: 'Rank', minWidth: 1/3 },
    { id: 'name', label: 'Name', minWidth: 1/3 },
    {
      id: 'tweets',
      label: 'Tweets',
      align: 'right',
      format: (value) => value.toLocaleString('en-US'),
    },
  ];

  
  const collection_name = "PLACEHOLDER";
  function createRankings(data) {
    var rows = [];
    let c = 1;
    data.forEach(nft_collection => {
      rows.push({"rank" : c, "name" : collection_name, "tweets" : nft_collection["count"]});
      c += 1;
    });
    return rows
  }

export default function Rankings () {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const [rows, setRows] = React.useState([]);

  useEffect(() => {
    fetch('/api/analytic')
      .then(res => res.json())
      .then(data => {setRows(createRankings(data));});
  }, []);
  fetch('/api/analytic').then(res => res.json()).then(data => {createRankings(data);});
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  
  return(
    <Container style={{marginTop: '10%'}}>
      
    <Paper sx={{ width: '100%', overflow: 'hidden' }}>
    <Typography sx={{fontSize: '3rem', marginLeft: '5%'}} color="white" align="left">Trending NFTs</Typography>
      <TableContainer sx={{ maxHeight: 7/10, width: '90%', marginTop: '5%' }}>
        <Table stickyHeader aria-label="sticky table" sx={{
      [`& .${tableCellClasses.root}`]: {
          borderBottom: "none"
          }
          }}>
          <TableHead>
            <TableRow>
              {columns.map((column) => ( 
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: 1/5, color: 'white'}}>
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
              {/* .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage) */}
              {rows.map((row) => {
                console.log("hi");
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.code} sx = {{height: 60}}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      return (
                        <TableCell key={column.id} align={column.align} style={{fontSize: 20, color: 'white'}}>
                          {column.format && typeof value === 'number'
                            ? column.format(value)
                            : value}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        component="div"
        count={rows.length}
        rowsPerPage={10}
        page={page}
        onPageChange={handleChangePage}
        style = {{color: 'white'}}
      />
    </Paper>
    </Container>
  );
      
    
}