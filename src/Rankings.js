import React, { Component } from 'react';
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
  
  function createData(rank, name, tweets, size) {
    return { rank, name, tweets, size };
  }
  const rows = [
    createData('1', 'IN', 1324171354, 3287263),
    createData('2', 'CN', 1403500365, 9596961),
    createData('3', 'IT', 60483973, 301340),
    createData('4', 'US', 327167434, 9833520),
    createData('5', 'CA', 37602103, 9984670),
    createData('6', 'AU', 25475400, 7692024),
    createData('7', 'DE', 83019200, 357578),
    createData('8', 'IE', 4857000, 70273),
    createData('9', 'MX', 126577691, 1972550),
    createData('10', 'JP', 126317000, 377973),
    createData('11', 'FR', 67022000, 640679),
    createData('12', 'GB', 67545757, 242495),
    createData('13', 'RU', 146793744, 17098246),
    createData('14', 'NG', 200962417, 923768),
    createData('15', 'BR', 210147125, 8515767),
  ];
  
  
export default function Rankings () {
    
        const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

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
                        style={{ minWidth: 1/5, color: 'white'}}
                      >
                        {column.label}
                      </TableCell>
                    ))}
                  </TableRow>
                </TableHead>
                <TableBody>
                  {rows
                    .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                    .map((row) => {
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