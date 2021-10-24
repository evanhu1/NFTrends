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
import eventBus from './eventBus';
const collectionName = [
  ('weewee',1000),('peepee',500)
]
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
  
  function createData(rank, name, tweets) {
    return {rank, name, tweets};
  }
  const rows = [];
  function getNFTs() {
    url = '';
    let getUrl = url + '/api/analytics';
    try {
      let NFTAnalytics =  fetch(getUrl);
      return  NFTAnalytics.json();
    }catch (error){
      console.log(error);
    } 
  }
  function createRankings(){
    let rankings = getNFTs();
    const i = 1;
    rankings.forEach(ranking=>{
      rows.push(createData(i, ranking[id], ranking[count]));
    });
  }
  
  
export default function Rankings () {
  createRankings();
        const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };
  // function dispatchNFT(id){
  //   console.log("sendingNFT");
  //   eventBus.dispatch("selectNFT", { name: id });
  // }
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
                              <TableCell onClick = {dispatchNFT(row[1])} key={column.id} align={column.align} style={{fontSize: 20, color: 'white'}}>
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